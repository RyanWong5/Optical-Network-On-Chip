#  Copyright 2016 The TensorFlow Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import tensorflow as tf
import os

import config_data

parser = argparse.ArgumentParser()
parser.add_argument('--batch_size', default=100, type=int, help='batch size')
parser.add_argument('--train_steps', default= 500000 , type=int,
                    help='number of training steps')

def main(argv):
    args = parser.parse_args(argv[1:])
    # Fetch the data
    (train_x, train_y), (test_x, test_y) = config_data.load_data()

    # Feature columns describe how to use the input.
    my_feature_columns = []
    for key in train_x.keys():
        my_feature_columns.append(tf.feature_column.numeric_column(key=key))


    # Build 2 hidden layer DNN with 10, 10 units respectively.
    classifier = tf.estimator.DNNClassifier(
        feature_columns=my_feature_columns,
        # Two hidden layers of 10 nodes each.
        hidden_units=[5000, 5000, 5000, 5000 ],
        #Specify Activation functions
        activation_fn = tf.nn.sigmoid,
        # The model must choose between 3 classes.
        n_classes=3)
        # Specify a place to save the model
#        model_dir = os.getcwd()+'/ModelSR')
    

    # Train the Model.
    classifier.train(
        input_fn=lambda:config_data.train_input_fn(train_x, train_y,
                                                 args.batch_size),
        steps=args.train_steps)

    # Evaluate the model.
    eval_result = classifier.evaluate(
        input_fn=lambda:config_data.eval_input_fn(test_x, test_y,
                                                args.batch_size))

    print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))

    exit()
    # Generate predictions from the model
    expected = ['Average', 'Bad', 'Good']
    predict_x = {
        'node0': [0, 11, 13],
        'node1': [1, 5, 7],
        'node2': [2, 6, 14],
        'node3': [3, 13, 11],
        'node4': [4, 2, 9],
        'node5': [5, 14, 10],
        'node6': [6, 3, 1],
        'node7': [7, 10, 15],
        'node8': [8, 4, 0],
        'node9': [9, 9, 8],
        'node10': [10, 8, 4],
        'node11': [11, 15, 12],
        'node12': [12, 12, 2],
        'node13': [13, 1, 5],
        'node14': [14, 7, 3],
        'node15': [15, 2, 6],

#        'SepalWidth': [3.3, 3.0, 3.1],
#        'PetalLength': [1.7, 4.2, 5.4],
#        'PetalWidth': [0.5, 1.5, 2.1],
    }

    predictions = classifier.predict(
        input_fn=lambda:config_data.eval_input_fn(predict_x,
                                                labels=None,
                                                batch_size=args.batch_size))

    template = ('\nPrediction is "{}" ({:.1f}%), expected "{}"')

    for pred_dict, expec in zip(predictions, expected):
        class_id = pred_dict['class_ids'][0]
        probability = pred_dict['probabilities'][class_id]

        print(template.format(config_data.SPECIES[class_id],
                              100 * probability, expec))


if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run(main)
