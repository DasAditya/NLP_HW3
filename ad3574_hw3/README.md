Commands to execute:

Q4

python3 parser.py q4 parse_train.dat parse_train.RARE.dat

Q5

python3 parser.py q5 parse_train.RARE.dat parse_dev.dat q5_prediction_file
python3 eval_parser3.py parse_dev.key q5_prediction_file > q5_eval.txt

Q6

python3 parser.py q4 parse_train_vert.dat parse_train_vert.RARE.dat
python3 parser.py q6 parse_train_vert.RARE.dat parse_dev.dat q6_prediction_file
python3 eval_parser3.py parse_dev.key q6_prediction_file > q6_eval.txt
