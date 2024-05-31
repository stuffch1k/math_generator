from generators import *

# идентификаторы генераторов
GENERATOR_UUID = {
    '77d65971-cc85-4455-0723-1f21a82b88f1': GenerateMatrixSizeTask,
    'b22fae57-4b10-4d50-740a-06956656bef1': GenerateMatrixElementTask,
    'c4703c4b-e322-4b5c-7c6c-d1652ce84bd8': GenerateMatrixSummTask,
    '028c1f3c-e728-46a1-3d3f-d037aa1c813d': GenerateMatrixNumberMultiplicationTask,
    '0c2f20c6-9191-41da-14e7-5e858bbb7fd7': GenerateMatrixTransposeTask,
    '4f6241db-b8b2-4cf0-182b-9d468f0a2d83': GenerateMatrixMultiplicationTask,
    'f26bf9ac-89fb-4698-cd53-26ca6fc4702a': GenerateFindDeterminantTask,
    '3b5b6b10-c9a5-4358-0079-3e9459f53f9f': GenerateDeterminantEquationTask,
    'f1579922-863b-424f-2044-edd7c3bd437a': GenerateFindReverseMatrixTask,
    'b07318ac-c462-4d51-9f25-052c36eb4d3f': GenerateFindReversedMatrixElementTask,
    '878f9145-3557-493a-01d3-0aa168edc6a7': GenerateFindMatrixRankTask,
    '7ae48f49-aecf-4006-c95d-af63a3260eb0': GenerateSolveMatrixEquationTask,
    '6463aa54-da58-4751-8578-72ab9670ec74': GenerateSolveDoubleMatrixEquationTask,
    'd53761d3-4270-4af4-5f21-b7caaa4efb43': GenerateSolveLinearEquationTask,
    'c4703c4b-e322-4b5c-7c6c-d1652ce84bd8': GenerateScalarVectorMultiplicationTask,
    'aa371420-8767-4dd4-1713-2968822580b0': GenerateVectorVectorMultiplicationTask,
    '6c94bbe5-2391-46dd-66ee-68ed3286d073': GenerateVectorVectorMultiplicationModuleTask
}

GENERATOR_TOPIC = {
    'Матрицы': ['77d65971-cc85-4455-0723-1f21a82b88f1', 'b22fae57-4b10-4d50-740a-06956656bef1', 
                'c4703c4b-e322-4b5c-7c6c-d1652ce84bd8', '028c1f3c-e728-46a1-3d3f-d037aa1c813d', 
                '0c2f20c6-9191-41da-14e7-5e858bbb7fd7', '4f6241db-b8b2-4cf0-182b-9d468f0a2d83'],
    'Определители': ['f26bf9ac-89fb-4698-cd53-26ca6fc4702a', '3b5b6b10-c9a5-4358-0079-3e9459f53f9f'],
    'Обратная матрица': ['f1579922-863b-424f-2044-edd7c3bd437a', 'b07318ac-c462-4d51-9f25-052c36eb4d3f'],
    'Ранг': ['878f9145-3557-493a-01d3-0aa168edc6a7'],
    'Матричные уравнения':['7ae48f49-aecf-4006-c95d-af63a3260eb0', '6463aa54-da58-4751-8578-72ab9670ec74'],
    'Системы линейных уравнений':['d53761d3-4270-4af4-5f21-b7caaa4efb43'],
    'Скалярное, векторное, смешанное произведение векторов':['c4703c4b-e322-4b5c-7c6c-d1652ce84bd8', 
                                                             'aa371420-8767-4dd4-1713-2968822580b0',
                                                             '6c94bbe5-2391-46dd-66ee-68ed3286d073']
}

