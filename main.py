from kwork import Kwork
import asyncio
import json
import os


async def main():
    api = Kwork(login=os.getenv('LOGIN'), password=os.getenv('PASSWORD'))
    # profile = await api.get_me()
    # print(profile)

    # categories = await api.get_categories()
    # print(categories)

    projects = await api.get_projects(categories_ids=[11])
    # print(projects)

    with open('projects.json', 'w') as file:
        json.dump(projects, file, indent=4, ensure_ascii=False)

    await api.close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
