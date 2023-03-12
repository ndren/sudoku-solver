document.body.style.zoom = 1.3
grid = document.getElementById("problems");
fetch("/problems").then(function(response) {
	return response.text();
}).then(function(data) {
	return JSON.parse(data);
}).then(function(problems) {
	let color_index = 0;
	let green_shift = 0;
	for (const problem of problems) {
		const sudoku = problem[0];
		const time = parseFloat(problem[1]).toPrecision(2);
		const timestamp = document.createElement("div");
		timestamp.innerText = "The sudoku below was completed by the server in " + time + " seconds, or " + time * 1000 + " milliseconds.";
		const sudokuElement = document.createElement("div");
		sudokuElement.style.padding = "25px";
		sudokuElement.style.paddingTop = "10px";
		sudokuElement.appendChild(timestamp);
		grid.appendChild(sudokuElement);
		for (let i=0; i<9; i++) {
			const rowElement = document.createElement("div");
			for (let j=0; j<9; j++) {
				const squareElement = document.createElement("span");
				squareElement.innerText = sudoku[i*9+j];
				rowElement.appendChild(squareElement);
				
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
})