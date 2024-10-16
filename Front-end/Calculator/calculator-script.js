// Get all the buttons
const buttons = document.querySelectorAll('.button');

// Get the display screen
const display = document.getElementById('display');

// Function to handle button and keyboard input
function inputHandler(value) {
    // Function to revert display to zero after 0.5 seconds
    function revertToZero() {
        setTimeout(() => {
            display.innerText = '0';
        }, 50); // Display for 0.5 seconds
    }

    // Helper function to check if input length exceeds the limit
    function checkLength() {
        return display.innerText.length >= 17;
    }

    // Helper function to check if the last character is an operator
    function isLastCharOperator() {
        const operators = ['%', '/', '*', '-', '+', '(', ')'];
        return operators.includes(display.innerText.slice(-1));
    }

    if (display.innerText === '' || display.innerText === '0') {
        // Show full names when screen is empty or shows 0
        if (value === '=') {
            display.innerText = '0';
            revertToZero();
        } else if (value === 'Delete') {
            display.innerText = '0';
            revertToZero();
        } else if (value === 'C') {
            display.innerText = '0';
            revertToZero();
        } else {
            // Add number to display
            display.innerText = value;
        }
    } else {
        // Handle input length limit
        if (checkLength() && value !== 'C' && value !== 'Delete' && value !== '=') {
            // Show message and prevent further input
            alert('Enter no more than 17 value.');
            return; // Prevent further input if length limit is exceeded
        }

        // Prevent writing the same operator twice in a row
        if (isLastCharOperator() && ['%', '/', '*', '-', '+', '(', ')'].includes(value)) {
            return; // Do nothing if the last character is an operator and the new value is also an operator
        }

        // Perform usual actions for other cases
        if (value === '=') {
            try {
                display.innerText = eval(display.innerText);
                if (display.innerText === 'undefined') {
                    display.innerText = 'error';
                    setTimeout(() => {
                        display.innerText = '0';
                    }, 500); // Show error for 0.5 seconds
                }
            } catch {
                display.innerText = 'error';
                setTimeout(() => {
                    display.innerText = '0';
                }, 500); // Show error for 0.5 seconds
            }
        } else if (value === 'Delete') {
            display.innerText = display.innerText.slice(0, -1);
        } else if (value === 'C') {
            display.innerText = '';
            revertToZero(); // Clear display and revert to zero
        } else {
            // Append the value to the display
            display.innerText += value;
        }
    }
}

// Add event listener to each button for mouse clicks
buttons.forEach(button => {
    button.addEventListener('click', () => {
        let value = button.innerText;
        // Check if the button has an image inside, indicating the delete button
        if (button.classList.contains('img')) {
            value = 'Delete';
        }
        inputHandler(value);
    });
});

// Add event listener for keyboard input
document.addEventListener('keydown', (event) => {
    const key = event.key;

    // Map keyboard keys to corresponding calculator actions
    const validKeys = '0123456789+-*/.()';
    if (validKeys.includes(key)) {
        inputHandler(key);
    } else if (key === 'Enter') {
        inputHandler('=');
    } else if (key === 'Backspace' || key === 'Delete') {
        inputHandler('Delete');
    }
});

// Initialize the calculator on page load
display.innerText = '0'; // Start with "0" on display
