// Set max date to today
document.getElementById('birthdate').max = new Date().toISOString().split('T')[0];

function calculateAge() {
    // Get the input date
    const birthdateInput = document.getElementById('birthdate').value;
    const errorDiv = document.getElementById('error');
    const resultDiv = document.getElementById('result');

    // Hide previous results and errors
    errorDiv.classList.add('hidden');
    resultDiv.classList.add('hidden');

    // Validate input
    if (!birthdateInput) {
        showError('Please select your date of birth!');
        return;
    }

    const birthDate = new Date(birthdateInput);
    const today = new Date();

    // Check if birthdate is in the future
    if (birthDate > today) {
        showError('Birth date cannot be in the future!');
        return;
    }

    // Calculate age
    let years = today.getFullYear() - birthDate.getFullYear();
    let months = today.getMonth() - birthDate.getMonth();
    let days = today.getDate() - birthDate.getDate();

    // Adjust for negative days
    if (days < 0) {
        months--;
        const prevMonth = new Date(today.getFullYear(), today.getMonth(), 0);
        days += prevMonth.getDate();
    }

    // Adjust for negative months
    if (months < 0) {
        years--;
        months += 12;
    }

    // Calculate additional information
    const totalDays = Math.floor((today - birthDate) / (1000 * 60 * 60 * 24));
    const totalHours = totalDays * 24;
    
    // Calculate next birthday
    let nextBirthday = new Date(today.getFullYear(), birthDate.getMonth(), birthDate.getDate());
    if (nextBirthday < today) {
        nextBirthday.setFullYear(today.getFullYear() + 1);
    }
    const daysUntilBirthday = Math.ceil((nextBirthday - today) / (1000 * 60 * 60 * 24));

    // Get day of week
    const daysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    const dayOfWeek = daysOfWeek[birthDate.getDay()];

    // Display results with animation
    displayResults(years, months, days, totalDays, totalHours, daysUntilBirthday, dayOfWeek);
}

function displayResults(years, months, days, totalDays, totalHours, daysUntilBirthday, dayOfWeek) {
    // Animate numbers
    animateValue('years', 0, years, 1000);
    animateValue('months', 0, months, 1000);
    animateValue('days', 0, days, 1000);
    
    // Set additional info
    document.getElementById('totalDays').textContent = totalDays.toLocaleString();
    document.getElementById('totalHours').textContent = totalHours.toLocaleString();
    document.getElementById('nextBirthday').textContent = daysUntilBirthday + ' days';
    document.getElementById('dayOfWeek').textContent = dayOfWeek;

    // Show result section
    document.getElementById('result').classList.remove('hidden');
}

function animateValue(id, start, end, duration) {
    const element = document.getElementById(id);
    const range = end - start;
    const increment = range / (duration / 16);
    let current = start;

    const timer = setInterval(() => {
        current += increment;
        if ((increment > 0 && current >= end) || (increment < 0 && current <= end)) {
            current = end;
            clearInterval(timer);
        }
        element.textContent = Math.floor(current);
    }, 16);
}

function showError(message) {
    const errorDiv = document.getElementById('error');
    errorDiv.textContent = message;
    errorDiv.classList.remove('hidden');
}

// Add Enter key support
document.getElementById('birthdate').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        calculateAge();
    }
});
