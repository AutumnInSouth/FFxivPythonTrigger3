import glm


def transform_coordinate(coordinate: glm.vec3, matrix: glm.mat4):
    x = (coordinate.x * matrix[0][0]) + (coordinate.y * matrix[1][0]) + (coordinate.z * matrix[2][0]) + matrix[3][0]
    y = (coordinate.x * matrix[0][1]) + (coordinate.y * matrix[1][1]) + (coordinate.z * matrix[2][1]) + matrix[3][1]
    z = (coordinate.x * matrix[0][2]) + (coordinate.y * matrix[1][2]) + (coordinate.z * matrix[2][2]) + matrix[3][2]
    w = 1 / ((coordinate.x * matrix[0][3]) + (coordinate.y * matrix[1][3]) + (coordinate.z * matrix[2][3]) + matrix[3][3])
    return glm.vec3(x * w, y * w, z * w)
