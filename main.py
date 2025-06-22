# main.py

from services.riot_account import get_puuid
from services.match_history import get_match_list
from services.match_detail import get_match_detail


def main():
    game_name = input("Oyuncu ismi (örn. NickName): ").strip()
    tag_line = input("TagLine (örn. TR1): ").strip()

    puuid = get_puuid(game_name, tag_line)
    if not puuid:
        print("PUUID alınamadı.")
        return

    matches = get_match_list(puuid)
    if not matches:
        print("Maç geçmişi bulunamadı.")
        return

    print(f"\nSon {len(matches)} maç bulundu. İlk maç detayları:")
    match_id = matches[0]["matchId"]
    match = get_match_detail(match_id)

    if match:
        print("\nHarita:", match["matchInfo"]["mapId"])
        print("Oyun Modu:", match["matchInfo"]["gameMode"])
        print("Oyuncular:")
        for player in match["players"]:
            print(f"- {player['gameName']}#{player['tagLine']} - Kill: {player['stats']['kills']}")


if __name__ == "__main__":
    main()



