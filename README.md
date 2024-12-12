# DES Application

Welcome to the DES Application repository! This project is a powerful Data Extraction System designed to streamline data processing and extraction tasks for various applications. Below, you'll find details about the project, how to set it up, and how to contribute.

## Features

- **Data Processing**: Efficient extraction and processing of data.
- **Customizable**: Easily extend functionality to suit specific use cases.
- **User-Friendly**: Intuitive interfaces and clear documentation for ease of use.
- **Robust Architecture**: Designed for scalability and reliability.

## Prerequisites

Before setting up the DES Application, ensure you have the following installed on your system:

- [Python 3.8+](https://www.python.org/)
- Required Python packages (see [requirements.txt](requirements.txt))
- Git

## Installation

Follow these steps to set up the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/mhmdsh24/desapp.git
   ```

2. Navigate to the project directory:
   ```bash
   cd desapp
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app/gui.py
   ```

## Usage

1. Configure the application settings as needed.
2. Input your data through the GUI or predefined files.
3. Run the application to extract and process the data.
4. Review the results, which are saved or displayed as specified.

## Folder Structure

```
├── app/
│   ├── desv2.py          # Core logic for data extraction
│   ├── gui.py            # Graphical User Interface for the application
│   └── __pycache__/      # Cached files
├── assets/
│   └── code evaluation.py  # Scripts for code evaluation
├── des_history.db        # Database for storing historical data
├── DES_Test_Cases.csv    # Example test cases for validation
├── requirements.txt      # Python dependencies
└── README.md             # Project overview (this file)
```

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add a concise description of your changes"
   ```
4. Push your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions, suggestions, or issues, please contact:

- **Author**: Mohamad Chmaitilly
- **Email**: mjc09@mail.aub.edu
- **GitHub**: [mhmdsh24](https://github.com/mhmdsh24)

---

Thank you for using the DES Application!
