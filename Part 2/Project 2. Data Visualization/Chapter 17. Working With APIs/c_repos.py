import requests
import plotly.express as px


def get_request():
    url = "https://api.github.com/search/repositories?q=language:c&sort=stars"
    headers = {"Accept": "application/vnd.github.v3+json"}
    return requests.get(url, headers=headers)


def get_r_dic(r):
    return r.json()


def get_status_code(r):
    return r.status_code


def get_result_incompletion(d):
    return d["incomplete_results"]


def get_total_count(d):
    return d["total_count"]


def get_q_repos(d):
    return len(d["items"])


if __name__ == "__main__":
    r = get_request()
    d = get_r_dic(r)

    repos, stars, hover_txts = [], [], []
    for repo in d["items"]:
        repo_name = f"<a href='{repo['html_url']}'>{repo['name']}</a>"
        repo_stars = repo["stargazers_count"]
        hover_txt = f"{repo['name']} by {repo['owner']['login']} \
                    <br>{repo['description']}."
        #
        repos.append(repo_name)
        stars.append(repo_stars)
        hover_txts.append(hover_txt)

    fig = px.bar(
        x=repos,
        y=stars,
        title="⭐️ ⭐️ ⭐️ Most-Starred C Projects on "
        + "<a href='https://github.com'>GitHub</a> ⭐️ ⭐️ ⭐️",
        labels={"x": "🗃️ Repository", "y": "⭐️ Stars"},
        hover_name=hover_txts,
    )
    fig.update_traces(marker_color="SteelBlue", marker_opacity=0.6)
    fig.update_layout(
        title_x=0.5,
    )
    fig.show()
