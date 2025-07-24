🧪 Lead Gen Form Automation with Selenium
This project automates the process of filling out a Google Form using Python and Selenium. The form is designed to simulate a lead generation intake form for small business advertising, asking questions about industry type, ad spend, marketing channels, and readiness to get started.

The goal: control the browser to intelligently fill out form fields, just like a human would — but faster, more reliably, and repeatably.

🧠 Why I Made This
I created this as a hands-on way to learn Selenium and browser automation. The form itself is fake — just a playground for simulating how small businesses might interact with marketing onboarding flows.

Working with Selenium feels a bit like robotics for the browser: you’re writing step-by-step instructions to manipulate real elements on screen. It forces you to slow down, think through page structure, and plan your logic clearly.

📸 Demo
Here’s what it looks like in action:


Auto-filling a Google Form with simulated responses.

⚙️ What It Does
Opens a Google Form using Chrome

Fills out:

Industry text field (e.g. “Roofing”)

Ad spend amount via dropdown

Checkbox selections for marketing channels

Radio buttons for campaign readiness

Submits the form once all fields are filled

🧰 Tech Stack
Python 3

Selenium

ChromeDriver

🗺️ Project Structure
bash
Copy
Edit
leadgen-form-selenium/
│
├── main.py              # Script that runs the Selenium automation
├── requirements.txt     # Dependencies
├── README.md            # You're reading it!
└── screenshots/         # (Optional) Screenshots or screen recordings
🚀 Getting Started
1. Clone this repo
bash
Copy
Edit
git clone https://github.com/your-username/leadgen-form-selenium.git
cd leadgen-form-selenium
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Run the script
bash
Copy
Edit
python main.py
You’ll see Chrome open and begin interacting with the form.

✅ What I Learned
How to identify and interact with elements like:

Text inputs

Radio buttons

Checkboxes

Dropdowns

Scrolling into view and clicking hidden or off-screen elements

Dealing with dynamic loading and waits using WebDriverWait

Using XPath effectively to target specific form labels and options

💡 Next Steps / Ideas
Turn this into a form-filling bot that loops over CSV input

Export filled answers to a backend

Add headless support for background automation

Try solving reCAPTCHA or login flows

🤖 Final Thoughts
Selenium is more than just a testing tool — it’s an automation Swiss Army knife. Whether you're scraping data, filling out forms, or simulating workflows, it helps you learn how the web really works under the hood.

📫 Contact
Want to jam on automation ideas or projects like this?
[Your Name] – [your email or GitHub profile link]
