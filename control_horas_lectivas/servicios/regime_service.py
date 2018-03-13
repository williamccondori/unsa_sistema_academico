from control_horas_lectivas.models import Regime
from control_horas_lectivas.dtos.regime_dto import RegimeDto


class RegimeService(object):

    def get(self):
        regimes_dto = []
        regimes = Regime.objects.all()
        for regime in regimes:
            regimes_dto.append(RegimeDto(
                regime.id
                , regime.name
            ))
        return regimes_dto

    def save(self, regime_dto):
        if (regime_dto.Estado == 1):
            regime = Regime(
                name=regime_dto.Name
            )
            regime.save()
        elif (regime_dto.Estado == 2):
            regime = Regime.objects.filter(pk=regime_dto.Id)
            regime.update(
                name=regime_dto.Name
            )
        else:
            return

    def delete(self, regime_dto):
        regime = Regime.objects.filter(pk=regime_dto.Id)
        regime.delete()
