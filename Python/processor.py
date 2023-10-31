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
                if stat.find("/") != -1:
                    sorted_stat_list = sorted(stat.split(" / "))
                    all_stats_set.add(" / ".join(sorted_stat_list))
                else:
                    all_stats_set.add(stat)

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
