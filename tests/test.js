// tests/test.js

// This test file verifies a bug fix in script.js without any external dependencies.
// It mocks the necessary DOM elements and functions to test the logic in isolation.
// To run: node tests/test.js

// --- Mock DOM and Browser APIs ---
const mockDocument = {
    _elements: {},
    getElementById: function(id) {
        if (!this._elements[id]) {
            const newElement = {
                textContent: '',
                style: {},
            };
            // If this is the canvas, add a mock `getContext` to prevent errors.
            if (id === 'confettiCanvas') {
                newElement.getContext = function() {
                    return {
                        clearRect: function() {},
                        save: function() {},
                        translate: function() {},
                        rotate: function() {},
                        fillRect: function() {},
                        restore: function() {}
                    };
                };
            }
            // If this is the audio element, add a mock `play` function.
            if (id === 'clickSound') {
                newElement.play = function() {
                    return { catch: function() {} }; // The script chains a .catch()
                };
            }
            this._elements[id] = newElement;
        }
        return this._elements[id];
    },
    querySelector: function(selector) {
        const match = selector.match(/\[data-year="(\d+)"\]/);
        if (match) {
            const year = match[1];
            const id = `petal-${year}`;
            if (!this._elements[id]) {
                this._elements[id] = {
                    dataset: { year: year },
                    classList: {
                        _classes: new Set(),
                        add: function(className) { this._classes.add(className); },
                        contains: function(className) { return this._classes.has(className); }
                    }
                };
            }
            return this._elements[id];
        }
        return null; // For other selectors, return null
    },
    // Add a dummy event listener to prevent the script from crashing.
    // The DOMContentLoaded callback in the script sets up UI event handlers,
    // but our test calls the logic functions directly, so we don't need the
    // setup to run.
    addEventListener: function() {}
};

global.document = mockDocument;
// Mock the `window` object for the same reason. The script adds a resize listener
// which is not relevant for this logic test.
global.window = {
    addEventListener: function() {}
};
// `alert` is used in the script, so we mock it to prevent it from throwing an error.
global.alert = () => {};
// Mock browser animation frame API
global.requestAnimationFrame = function() {};
// `launchConfetti` and `playClickSound` are also called, mock them.
global.launchConfetti = () => {};
global.playClickSound = () => {};

// --- Load script.js content ---
const fs = require('fs');
// The script is in the root, and the test is in tests/, so the path is ../script.js
const scriptContent = fs.readFileSync(__dirname + '/../script.js', 'utf8');

// --- Test Setup ---
// To access the script's internal functions and variables, we'll `eval` the script
// and attach the necessary components to the `global` object for the test.
const modifiedScriptContent = scriptContent + `
    global.clickedPetals = clickedPetals;
    global.handlePetalClick = handlePetalClick;
    global.nextMemory = nextMemory;
`;

// Run the modified script
eval(modifiedScriptContent);

// --- Test Runner ---
function assert(condition, message) {
    if (!condition) {
        console.error(`❌ Assertion failed: ${message}`);
        process.exit(1); // Exit with a non-zero code to indicate failure
    }
    console.log(`✅ Assertion passed: ${message}`);
}

console.log("--- Running Bug Fix Verification Test ---");

// --- Test Case ---

// 1. Set initial state.
// The `clickedPetals` set should be empty at the start.
assert(clickedPetals.size === 0, "Initial state: clickedPetals set is empty.");

// 2. Simulate a user clicking on the first petal.
const petal1 = document.querySelector('.petal[data-year="1"]');
handlePetalClick({ currentTarget: petal1 }); // This function is from script.js

// 3. Verify the state after the first click.
assert(clickedPetals.has(1), "After clicking petal 1, clickedPetals contains 1.");
assert(petal1.classList.contains('clicked'), "Petal 1 has the 'clicked' class.");

// 4. The `showMemory` function would update the modal title. We simulate this.
const modalTitle = document.getElementById('modalTitle');
modalTitle.textContent = "Year 1 - The Beginning"; // The content doesn't matter, just the number.

// 5. Simulate the user clicking the "Next Memory" button.
nextMemory(); // This is the function with the bug.

// 6. Verify the fixed behavior.
// Now that the bug is fixed, the state for year 2 should be updated.
// This assertion should now pass, confirming the fix.
assert(clickedPetals.has(2), "FIX VERIFIED: clickedPetals now contains 2 after 'nextMemory()'.");

const petal2 = document.querySelector('.petal[data-year="2"]');
assert(petal2.classList.contains('clicked'), "FIX VERIFIED: Petal 2 now has the 'clicked' class.");

console.log("\n--- Test successfully verified the fix. ---");
console.log("The test confirmed that `nextMemory()` now correctly updates the application state.");
