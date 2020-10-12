package idwall.desafio.string;

import java.util.ArrayList;
import java.util.List;

public class IdwallFormatter implements StringFormatter {

    public IdwallFormatter(int lineCharLimit, boolean shouldJustify) {
        this.lineCharLimit = lineCharLimit;
        this.shouldJustify = shouldJustify;
    }

    public final int lineCharLimit;
    public final boolean shouldJustify;

    /**
     * {@inheritDoc}
     */
    @Override
    public String format(String text) {
        final List<String> justifiedLines = new ArrayList<>();

        String[] words = text.split(" ");

        int length = words.length;
        int i = 0;

        while (i < length) {
            int start = i;
            int lineLength = words[i].length();
            int count = 0;

            while (i + 1 < length && lineLength + words[i + 1].length() + count < lineCharLimit) { //should have one more word
                i++;
                count++;
                lineLength += words[i].length();
            }

            final StringBuilder stringBuilder = new StringBuilder();

            final int neededSpaces = lineCharLimit - lineLength;
            final int wordsCount = i - start;
            final boolean lastLine = i == words.length - 1;

            int numSpaces = 0;
            if (wordsCount > 0) numSpaces = shouldJustify ? neededSpaces / wordsCount : 1;

            final int evenSpaces = numSpaces * wordsCount;
            int spacesLeft = neededSpaces - evenSpaces;

            for (int j = start; j <= i; j++) {
                stringBuilder.append(words[j]);
                boolean isLastWord = j + 1 <= i;
                if (isLastWord) stringBuilder.append(" ".repeat(numSpaces));
                if (!lastLine && spacesLeft-- > 0 && shouldJustify) stringBuilder.append(" ");

            }
            justifiedLines.add(stringBuilder.toString());
            i++;
        }

        return String.join("\n", justifiedLines);
    }


}
