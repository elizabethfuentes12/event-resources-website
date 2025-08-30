from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins,
    RemovalPolicy,
    CfnOutput
)
from constructs import Construct


class WebSiteStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # S3 bucket COMPLETAMENTE PRIVADO - NO PÚBLICO
        bucket = s3.Bucket(
            self, "EventWebsiteBucket",
            public_read_access=False,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True
        )

        # Origin Access Identity - SOLO CloudFront puede acceder
        oai = cloudfront.OriginAccessIdentity(
            self, "EventWebsiteOAI",
            comment="OAI for private Event Website"
        )

        # Dar permisos ÚNICAMENTE a CloudFront
        bucket.grant_read(oai)

        # CloudFront distribution - ÚNICA forma de acceso
        distribution = cloudfront.Distribution(
            self, "EventWebsiteDistribution",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.S3Origin(
                    bucket,
                    origin_access_identity=oai
                ),
                viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS
            ),
            default_root_object="index.html"
        )

        # Deploy del contenido web
        s3deploy.BucketDeployment(
            self, "DeployWebsite",
            sources=[s3deploy.Source.asset("./website")],
            destination_bucket=bucket,
            distribution=distribution,
            distribution_paths=["/*"]
        )

        # Outputs
        CfnOutput(
            self, "WebsiteURL",
            value=f"https://{distribution.distribution_domain_name}",
            description="URL del sitio web"
        )

        CfnOutput(
            self, "BucketName",
            value=bucket.bucket_name,
            description="Nombre del bucket S3"
        )
