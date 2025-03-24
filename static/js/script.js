// search bar
const data = [
    { name: "Home", url: "home" },
    { name: "Contribute Your Idea", url: "tips" },
    { name: "Give Solution", url: "tips" },
    { name: "Insights", url: "insights" },
    { name: "Tips", url: "tips" },
    { name: "Flag Concerns", url: "flag" },
    { name: "Get Started", url: " " },
    { name: "View Insights", url: "insights" },
    { name: "Suggest", url: "flag" },
    { name: "Report", url: "flag" },
    { name: "Government Helplines", url: "flag" },
    { name: "Send Report", url: "flag" }
];

function showResults() {
    const query = document.getElementById('searchBar').value.toLowerCase();
    const resultsContainer = document.getElementById('searchResults');
    resultsContainer.innerHTML = '';

    if (query.trim() === '') {
        resultsContainer.style.display = 'none';
        return;
    }

    const filteredResults = data.filter(item => item.name.toLowerCase().includes(query));

    if (filteredResults.length > 0) {
        resultsContainer.style.display = 'block';
        filteredResults.forEach(result => {
            const div = document.createElement('div');
            const link = document.createElement('a');
            link.href = result.url;
            link.textContent = result.name;
            link.style.display = 'block'; 
            link.classList.add('dropdown-item');
            div.appendChild(link); 
            resultsContainer.appendChild(div);
        });
    } else {
        resultsContainer.style.display = 'none'; 
    }
}

document.addEventListener("click", function (event) {
    const searchBar = document.getElementById('searchBar');
    const resultsContainer = document.getElementById('searchResults');

    // Check if the click is outside the search bar or results container
    if (!searchBar.contains(event.target) && !resultsContainer.contains(event.target)) {
        resultsContainer.style.display = 'none'; // Hide the dropdown
    }
});


///////////////////////////////////////////////////////////////////////////////////////////////////////////


document.addEventListener('DOMContentLoaded', function() {
    const resultSection = document.getElementById('resultSection');
    const predictBtn = document.getElementById('predictBtn');
    
    if (resultSection && !resultSection.classList.contains('hidden')) {
        setTimeout(function() {
            resultSection.scrollIntoView({ behavior: 'smooth' });
        }, 100);
    }
    
    document.getElementById('predictionForm').addEventListener('submit', function() {
        sessionStorage.setItem('scrollToResults', 'true');
    });
    
    if (sessionStorage.getItem('scrollToResults') === 'true') {
        sessionStorage.removeItem('scrollToResults');
        
        setTimeout(function() {
            if (resultSection) {
                resultSection.scrollIntoView({ behavior: 'smooth' });
            }
        }, 300);
    }
});


///////////////////////////////////////////////////////////////////////////////////////////////////////////



document.getElementById("sendBtn").addEventListener("click", function() {
    let textBox = document.getElementById("concernBox");
    
    if (textBox.value.trim() !== "") {
       textBox.value = ""; 
       alert("Sent!");
    }
 });
