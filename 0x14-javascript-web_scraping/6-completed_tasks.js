#!/usr/bin/node
// compute the number of completed tasks by user id

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const dict = {};
    const tasks = JSON.parse(body);
    for (const task of tasks) {
      if (task.completed) {
        if (task.userId in dict) {
          dict[task.userId] += 1;
        } else {
          dict[task.userId] = 1;
        }
      }
    }
    console.log(dict);
  }
});
