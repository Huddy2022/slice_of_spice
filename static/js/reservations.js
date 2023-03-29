//Get references from date and time input fields
const dateInput = document.querySelector('#date');
const timeInput = document.querySelector('#time');

// Add event listeners to input fields
dateInput.addEventListener('change', filterOptions);
timeInput.addEventListener('change', filterOptions);

//Define the filter options function and loop through each option to check availability
function filterOptions() {
    const selectedDate = dateInput.value;
    const selectedTime = timeInput.value;

    if (selectedDate && selectedTime) {
        const options = document.querySelectorAll('#table option');
        let isAvailable = false;
        for (const option of options) {
            if (option.dataset.available === 'True' && option.dataset.time === selectedTime) {
                isAvailable = true;
                option.disabled = false;
            } else {
                option.disbaled = true;
            }
        }
        if (!isAvailable) {
            alert('Sorry, there are no tables available for this date and time. Please select another date and time');
        }
    }
}