import sys

if __name__ == '__main__':
    mvn_version = sys.argv[1]
    s = mvn_version.split("-")

    # TODO - Check original and stratio versions with regex

    # e.x: 2.9.1-6.1.0-SNAPSHOT
    if len(s) == 3:
        if s[-1] == "SNAPSHOT":
            j_v, s_v, _ = s
            print(f"{j_v}+stratio.{s_v}.a0")

    # e.x: 3.5.0-1.0.0-PR1000-SNAPSHOT
    if len(s) == 4 and s[2].startswith("PR"):
        j_v, s_v, pr, _ = s
        pr_v = pr.replace("PR", "")
        print(f"{j_v}+stratio.{s_v}.dev{pr_v}")

