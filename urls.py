from views import Index, About, StudyPrograms, CoursesList, \
    CreateCourse, CreateCategory, CategoryList

routes = {
    '/': Index(),
    '/about/': About(),
    '/study-programs/': StudyPrograms(),
    '/courses-list/': CoursesList(),
    '/create-course/': CreateCourse(),
    '/create-category/': CreateCategory(),
    '/category-list/': CategoryList(),
}