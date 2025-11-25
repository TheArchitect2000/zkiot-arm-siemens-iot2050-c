import os
import logging
from PIL import Image
from rich import print
import torch
from transformers import AutoModelForCausalLM, AutoProcessor, GenerationConfig


class ConfigManager:
    """
    Manages configuration settings for the application.
    """
    def __init__(self, model_name, temp_dir="temp_dir", log_file="app.log"):
        self.model_name = model_name
        self.temp_dir = temp_dir
        self.log_file = log_file
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.dtype = torch.float16 if torch.cuda.is_available() else torch.float32

        # Validate and prepare the configuration
        self.validate()

    def validate(self):
        """
        Validates and prepares the configuration settings.
        """
        if not self.model_name:
            raise ValueError("Model name cannot be empty.")
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)
            print(f"[bold green]Temporary directory created at: {self.temp_dir}[/bold green]")

    def summary(self):
        """
        Prints a summary of the configuration settings.
        """
        print("[bold cyan]Configuration Summary:[/bold cyan]")
        print(f"  Model Name: {self.model_name}")
        print(f"  Temp Directory: {self.temp_dir}")
        print(f"  Log File: {self.log_file}")
        print(f"  Device: {self.device}")
        print(f"  Data Type: {self.dtype}")


class Logger:
    """
    Handles application logging.
    """
    @staticmethod
    def setup(log_file):
        """
        Sets up logging for the application.
        """
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )
        logging.info("Logging initialized.")
        print(f"[bold green]Logging enabled: {log_file}[/bold green]")

    @staticmethod
    def log(message, level="info"):
        """
        Logs a message at the specified level.
        """
        if level == "info":
            logging.info(message)
        elif level == "error":
            logging.error(message)
        elif level == "warning":
            logging.warning(message)


class ModelManager:
    """
    Handles loading, saving, and managing the ML model and processor.
    """
    def __init__(self, config):
        self.config = config
        self.model = None
        self.processor = None
        self.generation_config = None

    def initialize(self):
        """
        Initializes the model and processor, loading locally or remotely as needed.
        """
        if len(os.listdir(self.config.temp_dir)) == 0:
            print("[bold green]Loading model from remote repository...[/bold green]")
            Logger.log("Loading model from remote repository.")
            self.processor = AutoProcessor.from_pretrained(self.config.model_name, trust_remote_code=True)
            self.generation_config = GenerationConfig.from_pretrained(self.config.model_name)
            self.model = AutoModelForCausalLM.from_pretrained(
                self.config.model_name, torch_dtype=self.config.dtype, trust_remote_code=True
            ).to(self.config.device)
            self._save_model()
        else:
            print("[bold yellow]Loading model from local directory...[/bold yellow]")
            Logger.log("Loading model from local directory.")
            self.processor = AutoProcessor.from_pretrained(self.config.temp_dir, trust_remote_code=True)
            self.generation_config = GenerationConfig.from_pretrained(self.config.temp_dir)
            self.model = AutoModelForCausalLM.from_pretrained(
                self.config.temp_dir, torch_dtype=self.config.dtype, trust_remote_code=True
            ).to(self.config.device)
        print("[bold green]Model and processor initialized successfully.[/bold green]")

    def _save_model(self):
        """
        Saves the model and processor locally to the temp directory.
        """
        print("[bold green]Saving model and processor locally...[/bold green]")
        Logger.log("Saving model and processor locally.")
        self.processor.save_pretrained(self.config.temp_dir)
        self.model.save_pretrained(self.config.temp_dir)


class MedicalImageAnalyzer:
    """
    Encapsulates logic for analyzing medical images using the ML model.
    """
    def __init__(self, model_manager):
        self.model_manager = model_manager

    def load_image(self, image_path):
        """
        Loads an image from the given path on disk.
        """
        Logger.log(f"Loading image: {image_path}")
        if not os.path.exists(image_path):
            Logger.log(f"File not found: {image_path}", level="error")
            raise FileNotFoundError(f"The file {image_path} does not exist.")
        print(f"[bold blue]Loading image from: {image_path}[/bold blue]")
        return Image.open(image_path).convert("RGB")

    def generate_findings(self, image, prompt):
        """
        Generates findings for the given image and prompt using the model.
        """
        print(f"[bold yellow]Processing prompt: {prompt}[/bold yellow]")
        Logger.log(f"Processing prompt: {prompt}")
        try:
            inputs = self.model_manager.processor(
                images=[image], text=f"USER: <s>{prompt} ASSISTANT: <s>", return_tensors="pt"
            ).to(device=self.model_manager.config.device, dtype=self.model_manager.config.dtype)
            output = self.model_manager.model.generate(
                **inputs, generation_config=self.model_manager.generation_config
            )[0]
            response = self.model_manager.processor.tokenizer.decode(output, skip_special_tokens=True)
            Logger.log(f"Response generated for prompt: {prompt}")
            return response
        except Exception as e:
            Logger.log(f"Error during generation: {e}", level="error")
            raise RuntimeError(f"Error during generation for prompt: {prompt}")


class MedicalImageAnalysisWorkflow:
    """
    Orchestrates the end-to-end workflow for analyzing medical images.
    """
    def __init__(self, analyzer, anatomies=None):
        self.analyzer = analyzer
        self.anatomies = anatomies or [
            "Airway", "Breathing", "Cardiac", "Diaphragm",
            "Everything else (e.g., mediastinal contours, bones, soft tissues, tubes, valves, and pacemakers)"
        ]

    def run(self, image_path):
        """
        Executes the analysis workflow.
        """
        Logger.log(f"Starting analysis workflow for: {image_path}")
        print("[bold green]Starting analysis workflow...[/bold green]")
        try:
            image = self.analyzer.load_image(image_path)
            for anatomy in self.anatomies:
                prompt = f'Describe "{anatomy}"'
                response = self.analyzer.generate_findings(image, prompt)
                print(f"\n[bold cyan]Findings for [{anatomy}]:[/bold cyan]\n{response}\n")
        except Exception as e:
            Logger.log(f"Workflow error: {e}", level="error")
            print(f"[bold red]Error: {e}[/bold red]")


def main():
    # Setup configuration
    config = ConfigManager(
        model_name="StanfordAIMI/CheXagent-8b",
        temp_dir="temp_dir",
        log_file="medical_image_analysis.log"
    )
    config.summary()

    # Setup logging
    Logger.setup(config.log_file)

    # Initialize model manager and workflow
    model_manager = ModelManager(config)
    model_manager.initialize()
    analyzer = MedicalImageAnalyzer(model_manager)
    workflow = MedicalImageAnalysisWorkflow(analyzer)

    # Run the workflow
    workflow.run("Sample_images/Chest_sample1.jpg")


if __name__ == "__main__":
    main()
