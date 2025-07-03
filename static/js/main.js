document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('entryForm');
    const entriesTable = document.getElementById('entriesTable');
    const entries = JSON.parse(localStorage.getItem('entries') || '[]');

    // Load existing entries
    function loadEntries() {
        const tbody = entriesTable.querySelector('tbody');
        tbody.innerHTML = '';
        entries.forEach((entry, index) => {
            const row = tbody.insertRow();
            row.innerHTML = `
                <td>${index + 1}</td>
                <td>${entry.name}</td>
                <td>${entry.email}</td>
                <td>${entry.phone}</td>
                <td>${entry.address}</td>
                <td>
                    <button class="btn btn-danger btn-sm" onclick="deleteEntry(${index})">
                        Delete
                    </button>
                </td>
            `;
        });
    }

    // Save form data
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        const entry = {
            name: document.getElementById('name').value,
            email: document.getElementById('email').value,
            phone: document.getElementById('phone').value,
            address: document.getElementById('address').value
        };

        entries.push(entry);
        localStorage.setItem('entries', JSON.stringify(entries));
        form.reset();
        loadEntries();
        
        // Show success message
        const successAlert = document.getElementById('successAlert');
        successAlert.style.display = 'block';
        setTimeout(() => {
            successAlert.style.display = 'none';
        }, 3000);
    });

    // Delete entry
    function deleteEntry(index) {
        entries.splice(index, 1);
        localStorage.setItem('entries', JSON.stringify(entries));
        loadEntries();
    }

    // Initialize
    loadEntries();
});
