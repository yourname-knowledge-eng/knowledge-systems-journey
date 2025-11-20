# knowledge-systems-journey

print("🎯 بداية رحلة هندسة أنظمة المعرفة!")
print("=" * 50)

# تعريف العقد المعرفية الأولى
knowledge_nodes = []

class Concept:
    def __init__(self, name, description, category):
        self.name = name
        self.description = description 
        self.category = category
        self.relationships = []
    
    def add_relationship(self, target, relation_type):
        self.relationships.append({
            'target': target,
            'type': relation_type
        })
    
    def display(self):
        print(f"📚 المفهوم: {self.name}")
        print(f"   الوصف: {self.description}")
        print(f"   التصنيف: {self.category}")
        if self.relationships:
            print("   العلاقات:")
            for rel in self.relationships:
                print(f"     - {rel['type']}: {rel['target']}")

# إنشاء المفاهيم الأولى
ai = Concept("الذكاء الاصطناعي", "محاكاة الذكاء البشري في الآلات", "تقنية")
ml = Concept("تعلم الآلة", "القدرة على التعلم من البيانات دون برمجة صريحة", "تقنية")
data_eng = Concept("هندسة البيانات", "تصميم أنظمة جمع وتحويل وتخزين البيانات", "مهنة")

# إضافة العلاقات
ai.add_relationship(ml.name, "يشمل")
ml.add_relationship(data_eng.name, "يعتمد على")

# إضافة إلى القائمة
knowledge_nodes.extend([ai, ml, data_eng])

# عرض المفاهيم
print("🌱 العقد المعرفية التي أنشأتها:")
for node in knowledge_nodes:
    node.display()
    print("-" * 30)

print(f"✅ أنشأت {len(knowledge_nodes)} عقدة معرفية!")
print("🚀 استمر في الرحلة!")
