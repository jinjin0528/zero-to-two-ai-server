from typing import Mapping, Sequence

from modules.real_estate.application.dto.fetch_and_store_dto import RealEstateUpsertModel

class RealEstateReadPort(ABC):
    """매물 상세 조회용"""

    @abstractmethod
    def fetch_by_ids(self, ids: Sequence[int]) -> Mapping[int, RealEstateUpsertModel]:
        """real_estate_list_id -> 매물 DTO 매핑 반환"""
        raise NotImplementedError