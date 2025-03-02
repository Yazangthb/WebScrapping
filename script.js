document.addEventListener("DOMContentLoaded", () => {
    const tableBody = document.querySelector("#moviesTable tbody");
    const filterInput = document.getElementById("filterInput");
    let moviesData = [];
    let currentSort = { key: '', asc: true };
  
    // Fetch movies JSON data from an external file (e.g., movies.json)
    function fetchMovies() {
      fetch("movies.json")
        .then((response) => response.json())
        .then((data) => {
          moviesData = data;
          displayMovies(moviesData);
        })
        .catch((error) => console.error("Error fetching movies data:", error));
    }
  
    // Display movies in the table
    function displayMovies(data) {
      tableBody.innerHTML = "";
      data.forEach((movie) => {
        const tr = document.createElement("tr");
  
        // Title with link to movie details
        const titleTd = document.createElement("td");
        titleTd.innerHTML = `<a href="${movie.movie_url}" target="_blank">${movie.Title}</a>`;
        tr.appendChild(titleTd);
  
        // Release Year
        const yearTd = document.createElement("td");
        yearTd.textContent = movie.Year;
        tr.appendChild(yearTd);
  
        // Director
        const directorTd = document.createElement("td");
        directorTd.textContent = movie.Directed_by;
        tr.appendChild(directorTd);
  
        // Box Office
        const boxOfficeTd = document.createElement("td");
        boxOfficeTd.textContent = movie.Box_office;
        tr.appendChild(boxOfficeTd);
  
        tableBody.appendChild(tr);
      });
    }
  
    // Filter movies based on title input
    function filterMovies() {
      const filterValue = filterInput.value.toLowerCase();
      const filtered = moviesData.filter((movie) =>
        movie.Title.toLowerCase().includes(filterValue)
      );
      displayMovies(filtered);
    }
  
    // Sort movies by a given key (e.g., Title, Year)
    function sortMovies(key) {
      if (currentSort.key === key) {
        currentSort.asc = !currentSort.asc;
      } else {
        currentSort.key = key;
        currentSort.asc = true;
      }
  
      moviesData.sort((a, b) => {
        let valA = a[key];
        let valB = b[key];
  
        // Convert Year to number for proper numeric sort
        if (key === "Year") {
          valA = parseInt(valA);
          valB = parseInt(valB);
        }
  
        if (valA < valB) return currentSort.asc ? -1 : 1;
        if (valA > valB) return currentSort.asc ? 1 : -1;
        return 0;
      });
      // Apply current filter after sorting
      filterMovies();
    }
  
    // Add click event listeners to table headers for sorting
    document.querySelectorAll("#moviesTable th").forEach((header) => {
      header.addEventListener("click", () => {
        const key = header.getAttribute("data-key");
        sortMovies(key);
      });
    });
  
    // Add input event listener for filtering
    filterInput.addEventListener("input", filterMovies);
  
    // Initially load the movies data
    fetchMovies();
  });
  