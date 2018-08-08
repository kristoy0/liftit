from liftit import configparser


class TestConfigParser:
    def test_parsing(self):
        config = """
        build:
          image: golang:alpine
          ports:
            - '8080'
          steps:
            - go test
            - go build app

        deploy:
          image: alpine
          ports:
            - '8080:8080'
          command:
            - ./app
        """

        valid_dict = {
            "build": {
                "image": "golang:alpine",
                "ports": ["8080"],
                "steps": ["go test", "go build app"]
            },
            "deploy": {
                "image": "alpine",
                "ports": ["8080:8080"],
                "command": ["./app"]
            }
        }

        config_dict = configparser.validate_config(config)

        assert config_dict == valid_dict

    def test_parsing_fail(self):
        config = """
        deploy:
          image: alpine
          ports:
            - '8080:8080'
          command:
            - ./app
        """

        config_dict = configparser.validate_config(config)

        assert "Given YAML configuration is not valid:" in config_dict
