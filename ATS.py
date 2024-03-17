import tkinter as tk
from tkinter import filedialog
import fitz # Import PyMuPDF

class ApplicantTrackingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Applicant Tracking System")

        # Create widgets
        self.file_label = tk.Label(root, text="Upload Resume:")
        self.upload_button = tk.Button(root, text="Upload", command=self.upload_resume)
        self.requirements_label = tk.Label(root, text="Enter Job Requirements:")
        self.requirements_entry = tk.Entry(root, width=50)
        self.score_button = tk.Button(root, text="Calculate Score", command=self.calculate_score)
        self.result_label = tk.Label(root, text="Score:")

        # Layout widgets
        self.file_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.upload_button.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        self.requirements_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.requirements_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        self.score_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        self.result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def upload_resume(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                # Use PyMuPDF to read the PDF file
                doc = fitz.open(file_path)
                text = ""
                for page in doc:
                    text += page.get_text()
                self.resume_text = text
            except Exception as e:
                self.result_label.config(text=f"Error reading resume: {str(e)}")
                self.resume_text = None

    def calculate_score(self):
        if hasattr(self, 'resume_text') and self.resume_text:
            requirements = self.requirements_entry.get().lower()
            # Perform matching logic between resume text and job requirements
            score = self.match_requirements(self.resume_text, requirements)
            self.result_label.config(text=f"Score: {score}")
        else:
            self.result_label.config(text="No resume uploaded or reading error occurred.")

    def match_requirements(self, resume_text, requirements):
        # Example matching logic (dummy implementation)
        score = 0
        for word in requirements.split():
            if word in resume_text:
                score += 1
        return score

if __name__ == "__main__":
    root = tk.Tk()
    app = ApplicantTrackingSystem(root)
    root.mainloop()
