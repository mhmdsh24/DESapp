# DES Application

Welcome to the DES Application repository! This project is an implementation of the DES (Data Encryption Standard) algorithm, designed to demonstrate detailed encryption and decryption processes. The software showcases the results of each DES round and key expansion step, making it an excellent educational tool for understanding how DES works.

## Features

- **64-bit Block Encryption**: Encrypts and decrypts 64-bit data blocks using a 64-bit key.
- **Detailed Rounds Display**: Shows intermediate results after each DES round.
- **Key Expansion Visualization**: Displays key generation and expansion for each round.
- **Hexadecimal Input/Output**: Accepts message and key in hexadecimal format and displays results in hexadecimal.
- **User-Friendly Interface**: Intuitive GUI for inputting data and viewing results.

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

### Inputs
- **Message**: 16-character hexadecimal message or any text message that will be converted to 64-bit blocks.
- **Key**: 16-character hexadecimal key used for encryption and decryption.

### Outputs
- **Encryption Process**: Displays results for each round, including:
  - Key expansion for the round.
  - Intermediate results after operations like permutation and substitution.
  - Final ciphertext in hexadecimal.
- **Decryption Process**: Mirrors the encryption process to recover the original message.

## DES Algorithm Overview

### Key Generation
1. **Initial Permutation (PC-1)**: The 64-bit key is permuted and reduced to 56 bits.
2. **Splitting**: The 56-bit key is divided into two 28-bit halves.
3. **Round Shifts**: Each half undergoes left circular shifts according to a predefined schedule.
4. **Compression (PC-2)**: The shifted halves are permuted and compressed to generate a 48-bit subkey for each round.

### Encryption Steps
1. **Initial Permutation**: The 64-bit plaintext undergoes an initial permutation.
2. **Rounds (16 Total)**:
   - **Expansion (E)**: Expands the 32-bit right half to 48 bits.
   - **Key Mixing**: XORs the expanded data with the round subkey.
   - **Substitution (S-Boxes)**: Substitutes the XORed result using predefined S-Boxes to reduce it to 32 bits.
   - **Permutation (P)**: Permutes the substituted data.
   - **XOR with Left Half**: The permuted result is XORed with the left half of the data.
   - **Swap**: The left and right halves are swapped for the next round.
3. **Final Permutation**: After the 16 rounds, the halves are recombined and permuted to produce the ciphertext.

### Decryption Steps
- The decryption process reverses the encryption steps using the same subkeys in reverse order.

## Folder Structure

```
├── app/
│   ├── desv2.py          # Core logic for DES encryption and decryption
│   ├── gui.py            # Graphical User Interface for input/output
│   ├── test.py           # Test scripts for the DES implementation
│   └── __pycache__/      # Cached files
├── assets/
├── code evaluation.py    # Scripts for evaluating code functionality
├── des_history.db        # Database for storing encryption/decryption history
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
