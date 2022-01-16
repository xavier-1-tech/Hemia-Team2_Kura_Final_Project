resource "aws_ecs_cluster" "hemia-ecs-cluster" {
  name = "ecs-cluster-for-hemia"
}

resource "aws_ecs_service" "hemia-ecs-service-two" {
  name            = "hemia-app"
  cluster         = aws_ecs_cluster.hemia-ecs-cluster.id
  task_definition = aws_ecs_task_definition.hemia-ecs-task-definition.arn
  launch_type     = "FARGATE"
  network_configuration {
    subnets          = ["subnet-05t93f90b22ba76qx"]
    assign_public_ip = true
  }
  desired_count = 1
}

resource "aws_ecs_task_definition" "hemia-ecs-task-definition" {
  family                   = "ecs-task-definition-hemia"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  memory                   = "1024"
  cpu                      = "512"
  execution_role_arn       = "arn:aws:iam::123456789012:role/ecsTaskExecutionRole"
  container_definitions    = <<EOF
[
  {
    "name": "hemia-container",
    "image": "123456789012.dkr.ecr.us-east-1.amazonaws.com/hemia-repo:1.0",
    "memory": 1024,
    "cpu": 512,
    "essential": true,
    "entryPoint": ["/"],
    "portMappings": [
      {
        "containerPort": 80,
        "hostPort": 80
      }
    ]
  }
]
EOF
}