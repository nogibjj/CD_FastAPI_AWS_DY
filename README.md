# Ancient Chinese Poem Line Generator

[![Continuous Integration](https://github.com/nogibjj/DY_Template/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/DY_Template/actions/workflows/main.yml)
[![AWS CodeBuild](https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiSG5uQmUyM1VTeFp1eUtkUjRrT2RidENRYXRGRmYyVUwwWW9zZUhhQ2xoNnB2THdmYWduSHQ4Ny9LUVZUK2JwcFBkUUMyMEpjWFJJNGdQNmUzQldqUFRBPSIsIml2UGFyYW1ldGVyU3BlYyI6IjlEYjJDekFMOGE4NE4vL0MiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)

### Objective of this project

This project focus on creating a Microservice that returns JSON Payload and performs a Data Engineering related task. Continuous Integration shall be performed with Github Actions as well as Continuous Delivery with build server. In addtion, realistic API like FastAPI would be a great fit for demo.

My thought is to build an application that generate ancient Chinese poem line for people who are intested in learning. The poem library is provided by [今日诗词](https://www.jinrishici.com/). The application will return a JSON payload containing the poem line, title, author, and category. 

### Architectural & Workflow

![CI_CD_STACK](https://user-images.githubusercontent.com/81750079/204197207-2405823a-a3f3-498a-b4bf-0d4ef086cfc9.jpg)


### Example Output:

Link to the FastAPI swagger deployed on AWS App Runner: 

https://mmg24jdu7i.us-east-1.awsapprunner.com/docs#/

(If you are intested in this app, please contact author via issues, the APPRunner may be paused due to cost)

![image](https://user-images.githubusercontent.com/81750079/204179845-7f3e13a5-8150-43ee-a3c2-52241a4d4813.png)

Example JSON Payload
```
{
  "content": "洛阳城里春光好，洛阳才子他乡老。",
  "origin": "菩萨蛮",
  "author": "韦庄",
  "category": "古诗文-人生-青春"
}
```
