# Sudoku Solver
Written in Python 3  
Uses https://sudokusolver.app/ to get puzzels  
Uses boards as strings which you can export.  

Programmed with backtracking and trying to use 

Single Possibility Rule  
Hidden Single  



To run with Docker just run this command  
```bash
docker build -t sudoku_solver . && docker run -it sudoku_solver
```

To run the tests run the other dockerfile  
```bash
docker build -f Dockerfile_tests -t tests . && docker run -it tests
```
