# Definir el documento de política para la asunción del rol
data "aws_iam_policy_document" "eks_assume_role_policy" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["eks.amazonaws.com"]
    }
  }
}

# Definir el rol de IAM para el clúster EKS
resource "aws_iam_role" "eks-cluster-demo-new" {
  name               = "eks-cluster-demo-new"
  assume_role_policy = data.aws_iam_policy_document.eks_assume_role_policy.json
}

# Adjuntar la política AmazonEKSClusterPolicy al rol
resource "aws_iam_role_policy_attachment" "demo-AmazonEKSClusterPolicy" {
  role       = aws_iam_role.eks-cluster-demo-new.name  # Cambiado a .name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
}

# Crear el clúster EKS
resource "aws_eks_cluster" "demo" {
  name     = "demo-cluster"
  role_arn = aws_iam_role.eks-cluster-demo-new.arn  # Referencia al ARN del rol

  vpc_config {
    subnet_ids = [
      aws_subnet.private_us_east_1a.id,
      aws_subnet.private_us_east_1b.id
    ]
  }

  depends_on = [aws_iam_role_policy_attachment.demo-AmazonEKSClusterPolicy]
}

# Crear el proveedor de OIDC para el clúster EKS
resource "aws_iam_openid_connect_provider" "ekscluster" {
  client_id_list  = ["sts.amazonaws.com"]
  thumbprint_list = ["9e99a48a9960b14926bb7f3b3cf0b2b4f9bb9e3d"]
  url             = aws_eks_cluster.demo.identity[0].oidc[0].issuer
}
