mapred streaming -input hw1-rs8117/input -output hw1-rs8117/output-html -mapper "python mapper.py <ngram> <qno>" -reducer "python reducer.py" -file mapper.py -file reducer.py -numReduceTasks 1

There are 2 command line arguments to mapper.py.

<Ngram number> <question number>

Possible values:

ngram number => [1,2,3]
Question number => [2,3]