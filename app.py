<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>GitHub Events</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f9f9f9;
      padding: 30px;
    }

    h1 {
      color: #333;
    }

    ul {
      list-style-type: none;
      padding: 0;
    }

    li {
      background: #fff;
      margin-bottom: 10px;
      padding: 15px;
      border: 1px solid #ccc;
      border-radius: 6px;
      box-shadow: 0 1px 4px rgba(0, 0, 0, 0.1);
    }
  </style>
</head>
<body>
  <h1>📌 Latest GitHub Events</h1>
  <ul id="eventList"></ul>

  <script>
    function fetchEvents() {
      fetch("https://xxxxxx.ngrok-free.app/events")
        .then(response => response.json())
        .then(data => {
          const list = document.getElementById("eventList");
          list.innerHTML = "";

          data.forEach(event => {
            let text = "";
            const author = event?.sender?.login || "Someone";
            const time = event.timestamp || "some time ago";

            if (event.event === "push") {
              const branch = event.ref?.split("/").pop() || "unknown";
              text = `${author} pushed to ${branch} on ${time}`;
            } else if (event.event === "pull_request") {
              const from = event.pull_request?.head?.ref || "unknown";
              const to = event.pull_request?.base?.ref || "unknown";
              text = `${author} submitted a pull request from ${from} to ${to} on ${time}`;
            } else {
              text = `${author} triggered ${event.event} on ${time}`;
            }

            const li = document.createElement("li");
            li.textContent = text;
            list.appendChild(li);
          });
        })
        .catch(error => {
          console.error("❌ Failed to fetch events:", error);
        });
    }

    fetchEvents(); // Load on first open
    setInterval(fetchEvents, 15000); // Refresh every 15 seconds
  </script>
</body>
</html>
