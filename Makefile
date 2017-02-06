.phony:all

all:run

run:run.cpp
	$(CXX) -o $@ $^ 

clean:
	$(RM) -rf run
