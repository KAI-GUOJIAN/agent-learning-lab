import asyncio

import httpx


async def get_json(client: httpx.AsyncClient, url: str) -> dict:
    response = await client.get(url)
    response.raise_for_status()
    return response.json()


async def main():
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "agent-learning-lab",
    }

    async with httpx.AsyncClient(timeout=10.0, headers=headers) as client:
        try:
            user, repo = await asyncio.gather(
                get_json(client, "https://api.github.com/users/KAI-GUOJIAN"),
                get_json(
                    client,
                    "https://api.github.com/repos/modelcontextprotocol/python-sdk",
                ),
            )
        except httpx.HTTPStatusError as error:
            print(f"API 返回 HTTP {error.response.status_code}")
            return
        except httpx.RequestError as error:
            print(f"网络请求失败：{error}")
            return

    print(f"GitHub 用户：{user['login']}")
    print(f"公开仓库数：{user['public_repos']}")
    print(f"仓库：{repo['full_name']}")
    print(f"Stars：{repo['stargazers_count']}")


asyncio.run(main())