resource "aws_s3_bucket_lifecycle_configuration" "secureshop" {
  bucket = aws_s3_bucket.secureshop.id

  rule {
    id     = "cleanup-old-objects"
    status = "Enabled"

    abort_incomplete_multipart_upload {
      days_after_initiation = 7
    }

    expiration {
      days = 365
    }
  }
}