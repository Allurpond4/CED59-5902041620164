<?

namespace frontend\controllers;

use yii\web\Controller;

class TestController extends Controller{
    public function actionTest(){
        echo 'Hello World';

    }
    public function actionFern(){

        $data = 'data test';
        return $this->render('fern',['data' =>$data]);
    }
}


?>