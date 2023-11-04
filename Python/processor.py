class Processor:
    # Attributes
    _data = list()

    # Constructors
    def __init__(self, data):
        self._data = data

    # Methods
    def pre_process_characters_data_for_stat(self):
        all_stats_set = set()

        for character_data in self._data:
            stats_from_stats_list = [stat.split(";")[-1] for stat in character_data["stats"]]
            stats_from_substats_list = [substat for substat in character_data["substats"]]
            stats_list = stats_from_stats_list + stats_from_substats_list
            stats_set = set(stats_list)

            for stat in stats_set:
                all_stats_set.add(self._sort_stat_alphabetical_order(stat))

        all_stats_set = sorted(all_stats_set)

        return all_stats_set

    def pre_process_characters_data_for_slot(self):
        stats_slot_names_list = [name.split(";")[0] for name in self._data[0]["stats"]]
        substats_slot_names_list = self._get_slot_name_list("substats", "Substat")
        relics_slot_names_list = self._get_slot_name_list("relics", "Relic")
        ornaments_slot_names_list = self._get_slot_name_list("ornaments", "Ornament")

        all_slot_names = stats_slot_names_list + substats_slot_names_list + relics_slot_names_list + ornaments_slot_names_list

        return all_slot_names

    def _get_slot_name_list(self, key, slot_name):
        slot_sizes_set = set()

        for character_data in self._data:
            number_slots_from_key = len([slot for slot in character_data[key]])
            slot_sizes_set.add(number_slots_from_key)

        max_number_slots_from_key = max(slot_sizes_set)
        slot_names_list = ["{} {}".format(slot_name, i) for i in range(1, max_number_slots_from_key + 1)]

        return slot_names_list

    def pre_process_characters_data_for_character(self):
        characters_list = list()

        for character_data in self._data:
            name = character_data["name"]
            rarity = character_data["rarity"]
            type = character_data["type"]
            path = character_data["path"]

            characters_list.append((name, rarity, type, path))

        return characters_list

    def pre_process_characters_data_for_character_stat(self, storage):
        characters_stats_list = list()

        for character_data in self._data:
            name = character_data["name"]
            stats = character_data["stats"]
            substats = character_data["substats"]

            new_stats = ["{};{}".format(s.split(";")[0], self._sort_stat_alphabetical_order(s.split(";")[1])) for s in stats]
            new_substats = [self._sort_stat_alphabetical_order(s) for s in substats]
            new_substats = ["Substat {};{}".format(i + 1, new_substats[i]) for i in range(len(new_substats))]

            new_stats_and_substats = new_stats + new_substats

            for stat_or_substat in new_stats_and_substats:
                slot_name, stat = stat_or_substat.split(";")
                characters_stats_list.append((name, slot_name, stat))

        return characters_stats_list

    def _sort_stat_alphabetical_order(self, stat):
        if stat.find("/") != -1:
            sorted_stat_list = sorted(stat.split(" / "))
            return " / ".join(sorted_stat_list)
        else:
            return stat
