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
        substats_slot_sizes_set = set()
        relics_slot_sizes_set = set()
        ornaments_slot_sizes_set = set()

        for character_data in self._data:
            number_slots_from_substats = len([substat for substat in character_data["substats"]])
            number_slots_from_relics = len([relic for relic in character_data["relics"]])
            number_slots_from_ornaments = len([ornament for ornament in character_data["ornaments"]])

            substats_slot_sizes_set.add(number_slots_from_substats)
            relics_slot_sizes_set.add(number_slots_from_relics)
            ornaments_slot_sizes_set.add(number_slots_from_ornaments)

        max_number_slots_from_substats = max(substats_slot_sizes_set)
        max_number_slots_from_relics = max(relics_slot_sizes_set)
        max_number_slots_from_ornaments = max(ornaments_slot_sizes_set)

        stats_slot_names_list = [name.split(";")[0] for name in self._data[0]["stats"]]
        substats_slot_names_list = ["Substat {}".format(i) for i in range(1, max_number_slots_from_substats + 1)]
        relics_slot_names_list = ["Relic {}".format(i) for i in range(1, max_number_slots_from_relics + 1)]
        ornaments_slot_names_list = ["Ornament {}".format(i) for i in range(1, max_number_slots_from_ornaments + 1)]
        all_slot_names = stats_slot_names_list + substats_slot_names_list + relics_slot_names_list + ornaments_slot_names_list

        return all_slot_names
