package exercise.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class helloController() {
    @GetMapping("/hello")
    @ResponseBody

    public string helloWorld() {
        returns "Hello World!";
    }
}