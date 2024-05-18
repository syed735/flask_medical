# Multiple Disease Prediction

Welcome to the Multiple Disease Prediction web application! This is a major project developed for predicting multiple diseases such as diabetes, cancer, liver disease, lung disease, and kidney disease using machine learning models built with scikit-learn and TensorFlow.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## About

Multiple Disease Prediction is a web application designed to assist in the prediction of various diseases. By leveraging machine learning models, the app provides users with a tool to input their health data and receive predictions for diseases such as diabetes, cancer, liver disease, lung disease, and kidney disease.

## Features

- **User Authentication:** Sign up and log in securely.
- **Disease Prediction:** Predict multiple diseases using trained machine learning models.
- **User Dashboard:** View prediction results and manage your profile.
- **Responsive Design:** Accessible on both desktop and mobile devices.

## Tech Stack

- **Backend:** Flask, SQLAlchemy
- **Frontend:** HTML, CSS, JavaScript (Bootstrap for styling)
- **Machine Learning:** scikit-learn, TensorFlow
- **Database:** SQLite (for development)

## Getting Started

To get a local copy up and running, follow these steps:

### Prerequisites

- [Python](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Syed735/.gitflask-medical.git
    ```

2. Navigate to the project directory:
    ```sh
    cd RiskAssess-master
    ```

3. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

4. Activate the virtual environment:
    - On Windows:
      ```sh
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```sh
      source venv/bin/activate
      ```

5. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

6. Set up the database:
    ```sh
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

7. Run the application:
    ```sh
    flask run
    ```

    The application will be available at `http://127.0.0.1:5000`.

## Usage

1. **Sign Up:** Create a new account by providing your details.
2. **Log In:** Access your account using your credentials.
3. **Input Health Data:** Enter the required health information for disease prediction.
4. **Get Predictions:** View the predictions for multiple diseases based on your input data.
5. **Manage Profile:** View and update your profile and prediction history from the user dashboard.

## Contributing

We welcome contributions! Please follow these steps to contribute:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

Please make sure to update tests as appropriate.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact
Syed Sufiyan - sufiyanahmedsyed388@gmail.com

Project Link: https://github.com/Syed735/flask=medical/RiskAssess-master

---

*This README was generated with ❤️ by Sufiyan*

