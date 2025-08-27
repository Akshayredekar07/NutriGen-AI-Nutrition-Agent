# import os
# import yaml
# from dotenv import load_dotenv

# load_dotenv()


# class Config:

#     def __init__(self, config_file="config.yaml"):
#         with open(config_file, "r", encoding="utf-8") as f:
#             self.cfg = yaml.safe_load(f)
#         self.config = self._load_config()

#     def _resolve_env(self, value: str):
#         if isinstance(value, str) and value.startswith("${") and value.endswith("}"):
#             env_key = value[2:-1] 
#             return os.getenv(env_key, "")
#         return value

#     def _load_config(self):
#         config = {}
#         for section, values in self.cfg.items():
#             config[section] = {k: self._resolve_env(v) for k, v in values.items()}
#         return config


#     # Accessors for each service
#     @property
#     def supabase_url(self):
#         return self.config["supabase"]["url"]

#     @property
#     def supabase_key(self):
#         return self.config["supabase"]["key"]

#     @property
#     def postgres(self):
#         return self.config["postgres"]

#     @property
#     def google_api_key(self):
#         return self.config["google"]["api_key"]

#     @property
#     def grok_api_key(self):
#         return self.config["grok"]["api_key"]


#     @property
#     def langchain_api_key(self):
#         return self.config["langchain"]["api_key"]

#     @property
#     def langchain_project(self):
#         return self.config["langchain"]["project"]

#     @property
#     def langsmith_tracing(self):
#         return self.config["langsmith"]["tracing"]

#     @property
#     def langsmith_endpoint(self):
#         return self.config["langsmith"]["endpoint"]

#     @property
#     def langsmith_api_key(self):
#         return self.config["langsmith"]["api_key"]

#     @property
#     def langsmith_project(self):
#         return self.config["langsmith"]["project"]
    

#     def get_postgres_uri(self, sslmode: bool = True) -> str:
#         pg = self.postgres

#         # Construct the Supabase direct URL dynamically
#         uri = f"postgresql+psycopg://postgres.bsuynzzdscnuloeafyuc:{pg['password']}@aws-1-ap-south-1.pooler.supabase.com:5432/postgres"

#         if sslmode:
#             uri += "?sslmode=require"

#         return uri



# if __name__ == "__main__":
#     cfg = Config()
#     # print(cfg.get_postgres_uri())


    
#     # print("Supabase URL:", cfg.supabase_url)
#     # print("Supabase Key:", cfg.supabase_key)
#     # print("Postgres Config:", cfg.postgres)
#     # print("Google API Key:", cfg.google_api_key)
#     # print("Grok API Key:", cfg.grok_api_key)


#     # print("LangChain API Key:", cfg.langchain_api_key)



# # cfg = {
# #     "supabase": {
# #         "url": "${SUPABASE_URL}",
# #         "key": "${SUPABASE_KEY}"
# #     },
# #     "postgres": {
# #         "host": "${PGHOST}",
# #         "port": "${PGPORT}",
# #         "user": "${PGUSER}",
# #         "password": "${PGPASSWORD}",
# #         "database": "${PGDATABASE}"
# #     }
# # }


import os
import yaml
from dotenv import load_dotenv

load_dotenv()


class Config:

    def __init__(self, config_file="config.yaml"):
        with open(config_file, "r", encoding="utf-8") as f:
            self.cfg = yaml.safe_load(f)
        self.config = self._load_config()

    def _resolve_env(self, value: str):
        if isinstance(value, str) and value.startswith("${") and value.endswith("}"):
            env_key = value[2:-1]
            return os.getenv(env_key, "")
        return value

    def _load_config(self):
        config = {}
        for section, values in self.cfg.items():
            config[section] = {k: self._resolve_env(v) for k, v in values.items()}
        return config

    # ---------------- Accessors ----------------
    @property
    def supabase_url(self):
        return self.config.get("supabase", {}).get("url", "")

    @property
    def supabase_key(self):
        return self.config.get("supabase", {}).get("key", "")

    @property
    def postgres(self):
        return self.config.get("postgres", {})

    @property
    def google_api_key(self):
        return self.config.get("google", {}).get("api_key", "")

    @property
    def grok_api_key(self):
        return self.config.get("grok", {}).get("api_key", "")

    @property
    def langchain_api_key(self):
        return self.config.get("langchain", {}).get("api_key", "")

    @property
    def langchain_project(self):
        return self.config.get("langchain", {}).get("project", "")

    @property
    def langsmith_api_key(self):
        return self.config.get("langsmith", {}).get("api_key", "")

    @property
    def langsmith_project(self):
        return self.config.get("langsmith", {}).get("project", "")

    @property
    def langsmith_tracing_v2(self):
        # Default to "true" if not set
        return str(self.config.get("langsmith", {}).get("tracing_v2", "true")).lower()

    @property
    def langsmith_endpoint(self):
        return self.config.get("langsmith", {}).get("endpoint", "")

    # ---------------- Methods ----------------
    def get_postgres_uri(self, sslmode: bool = True) -> str:
        pg = self.postgres
        if not pg:
            raise ValueError("Postgres config not found")

        uri = f"postgresql+psycopg://{pg.get('user','')}:{pg.get('password','')}" \
              f"@{pg.get('host','')}:{pg.get('port','')}/{pg.get('database','')}"

        if sslmode:
            uri += "?sslmode=require"
        return uri


if __name__ == "__main__":
    cfg = Config()

    # print("Postgres URI:", cfg.get_postgres_uri())
    # print("Supabase URL:", cfg.supabase_url)
    # print("Supabase Key:", cfg.supabase_key)
    # print("Google API Key:", cfg.google_api_key)
    # print("Grok API Key:", cfg.grok_api_key)
    # print("LangChain API Key:", cfg.langchain_api_key)
    # print("LangSmith API Key:", cfg.langsmith_api_key)
