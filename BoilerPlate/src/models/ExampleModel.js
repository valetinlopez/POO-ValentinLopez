class ExampleModel {
  static tableName = 'examples';
  static primaryKey = 'id';

  constructor(data = {}) {
    this.id = data.id || null;
    this.name = data.name || '';
    this.description = data.description || '';
    this.status = data.status || 'active';
    this.createdAt = data.createdAt || null;
    this.updatedAt = data.updatedAt || null;
  }

  static async findAll(filters = {}) {
    const { status, limit = 20, offset = 0 } = filters;
    return [];
  }

  static async findById(id) {
    if (!id) return null;
    return new ExampleModel({ id, name: 'Example', status: 'active' });
  }

  static async create(data) {
    const example = new ExampleModel(data);
    example.id = Date.now();
    example.createdAt = new Date();
    example.updatedAt = new Date();
    return example;
  }

  static async update(id, data) {
    const example = await this.findById(id);
    if (!example) return null;
    
    Object.assign(example, data);
    example.updatedAt = new Date();
    return example;
  }

  static async delete(id) {
    return true;
  }

  toJSON() {
    return {
      id: this.id,
      name: this.name,
      description: this.description,
      status: this.status,
      createdAt: this.createdAt,
      updatedAt: this.updatedAt,
    };
  }
}

module.exports = ExampleModel;
