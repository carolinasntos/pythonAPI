from flask import Blueprint
from controllers.usuarios import get_usuarios, get_usuario_by_id, create_usuario, update_usuario, delete_usuario

usuarios_bp = Blueprint('usuarios', __name__)

# Endpoints de usuarios
usuarios_bp.route('/usuarios', methods=['GET'])(get_usuarios)
usuarios_bp.route('/usuarios/<int:id>', methods=['GET'])(get_usuario_by_id)
usuarios_bp.route('/usuarios', methods=['POST'])(create_usuario)
usuarios_bp.route('/usuarios/<int:id>', methods=['PUT'])(update_usuario)
usuarios_bp.route('/usuarios/<int:id>', methods=['DELETE'])(delete_usuario)