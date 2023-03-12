// Adapted from https://stackoverflow.com/a/69374442, CC BY SA 4.0
const form = document.getElementById('problem');
const solutions = document.getElementById('solutions'); // div
form.onsubmit = function(event){
        const xhr = new XMLHttpRequest();
        const formData = new FormData(form);
		solutions.innerHTML = '';

        xhr.open('POST','/solver')
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.send(JSON.stringify(Object.fromEntries(formData)));

        xhr.onreadystatechange = function() {

            if (xhr.readyState == XMLHttpRequest.DONE) {
				let color_index = 0;
				let green_shift = 0;
				const json = JSON.parse(xhr.response);
				const sudoku = json[0];
				const timeout = json[1];
				const solutions_found = sudoku.length;
				const message = document.createElement("p")
				if (timeout) {
					message.innerText = "The server could not handle your sudoku, it was too hard. "+solutions_found+" solution(s) were found.";
				} else {
					message.innerText = "The server found all "+solutions_found+" solution(s)!";
				}
				solutions.appendChild(message);
                for (const sudokuSolution of sudoku) {
					const sudokuElement = document.createElement("div")
					sudokuElement.style.padding = "25px";
					solutions.appendChild(sudokuElement);
					for (const rowSolution of sudokuSolution) {
						const rowElement = document.createElement("div");
						for (const squareSolution of rowSolution) {
							const squareElement = document.createElement("span");
							squareElement.innerText = squareSolution;
							color_level = Math.floor(255*color_index/8) 
							squareElement.style.color = "rgb("+(255-color_level)+","+(150-green_shift*10)+","+color_level+")"
							squareElement.style.padding = "1px"
							rowElement.appendChild(squareElement);
							color_index++;
							
							color_index = color_index % 9;
						}
						green_shift++;
						green_shift = green_shift % 9;
						sudokuElement.appendChild(rowElement);
					}
				}
            }
        }
        // This prevents the page from refreshing
        return false;
    }