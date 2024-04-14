//The plan


document.getElementById('addUnavailability').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form from submitting normally
    
    // Gather form data
    const employeeName = document.getElementById('employeeName').value;
    const date = document.getElementById('date').value;
    const startTime = document.getElementById('startTime').value;
    const endTime = document.getElementById('endTime').value;
    
    console.log("Employee Unavailability:", employeeName, date, startTime, endTime);
    
    // Here, you would typically send this data to the server via AJAX
});


/*

fetch('/api/data')
    .then(response => response.json())
    .then(data => {
        // Handle the response data
        console.log(data.message);  // Output: "Hello from the backend!"
    })
    .catch(error => {
        // Handle any errors
        console.error('Error fetching data:', error);
    });


USE JSON or FETCH
Modern Approach: Fetch API
fetch('https://api.example.com/data')
    .then(response => response.json()) // Parses the JSON response
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));

How AJAX Works:
An event occurs in a web page (the page is loaded, a button is clicked, etc.).
An XMLHttpRequest object is created by JavaScript.
The XMLHttpRequest object sends a request to a web server.
The server processes the request.
The server sends a response back to the web page.
The response is read by JavaScript.
Proper action (like updating the page) is performed by JavaScript.

Key Points:
Asynchronous: The client-side code makes an asynchronous call to the server, which allows the web page to continue processing while waiting for the server's response, enhancing the user experience.
JavaScript and the DOM: AJAX uses JavaScript to interact with the DOM (Document Object Model) to update the content dynamically.
XMLHttpRequest Object: This is the core technology behind AJAX. Modern implementations often use the Fetch API, which provides a more powerful and flexible feature set to perform network requests.

*/

//thanks GPT for getting me started 