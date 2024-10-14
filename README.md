
### poject structure
```
/user_diary
│
├── /venv
│
├── /static
│   ├── /css
│   ├── /js
│   └── /images
│
├── /templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── diary.html
│   └── settings.html
│
├── app.py
│
├── requirements.txt
│
├── runtime.txt
│
├── Procfile
│
└── README.md
```

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- MongoDB installed and running locally.

## Getting Started

Follow these steps to set up the project locally:

1. **Clone the Repository**

   Open your terminal and run the following command:

   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Enable Virtual Environment**

   Create and activate a virtual environment:

   ```bash
   # For Windows
   python -m venv venv
   venv\Scripts\activate

   # For macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**

   Install the required packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up MongoDB**

   Ensure that your MongoDB server is running. You may need to:

   - Start the MongoDB service.
   - Add the connection string provided by MongoDB to your application's configuration.

5. **Run the Application**

   Finally, run the application:

   ```bash
   python app.py
   ```

