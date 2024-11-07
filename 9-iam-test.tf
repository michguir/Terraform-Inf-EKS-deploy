data "aws_iam_policy_document" "test_oidc_assume_role_policy" {
  statement {
    actions = [ "sts:AssumeRoleWithWebIdentity" ]
    effect = "Allow"

    condition {
      test = "StringEquals"
      variable = "${replace(aws_iam_openid_connect_provider.ekscluster.url, "https://", "")}:sub"
      values = [
        "system:serviceaccount:default:aws-test"]
    }
    principals {
      identifiers = [
        aws_iam_openid_connect_provider.ekscluster.arn]
      type = "Federated"
    }

  }
}

resource "aws_iam_role" "test_oidc" {
    assume_role_policy = data.aws_iam_policy_document.test_oidc_assume_role_policy.json
    name = "test_oidc"
  }

resource "aws_iam_policy" "test-policy" {
    name = "test-policy"

    policy = jsonencode({
      Statement = [{
        Action = [
          "s3:ListAllMyBuckets",
          "s3:HeadBucket"
        ]
        Effect   = "Allow"
        Resource = "aws:aws:se:::*"
      }]
      Version = "2012-10-17"
    })
}

resource "aws_iam_policy_attachment" "test_attach" {
  name       = "test-attach"  # Nombre único para el attachment
  roles = [aws_iam_role.test_oidc.name]
  policy_arn = aws_iam_policy.test-policy.arn
}

output "test_policy_arn" {
  value = aws_iam_role.test_oidc.arn

}