resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.main.id  # Accediendo al ID de la VPC

  tags = {
    Name = "igw"
  }
}