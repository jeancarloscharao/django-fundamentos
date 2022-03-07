from ..models import Endereco


def listar_enderecos():
    enderecos = Endereco.objects.all()
    return enderecos


def listar_endereco_id(id):
    endereco = Endereco.objects.get(id=id)
    return endereco


def remover_endereco(endereco):
    endereco.delete()


def cadastrar_endereco(endereco):
    return Endereco.objects.create(
        rua=endereco.rua,
        numero=endereco.numero,
        complemento=endereco.complemento,
        bairro=endereco.bairro,
        cidade=endereco.cidade,
        estado=endereco.estado,
        pais=endereco.pais
    )


def editar_endereco(endereco, endereco_novo):
    endereco.rua = endereco_novo.rua
    endereco.numero = endereco_novo.numero
    endereco.complemento = endereco_novo.complemento
    endereco.bairro = endereco_novo.bairro
    endereco.cidade = endereco_novo.cidade
    endereco.estado = endereco_novo.estado
    endereco.pais = endereco_novo.pais
    endereco.save(force_update=True)
